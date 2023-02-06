# Import necessary modules first 
from sgnlp.models.sentic_gcn import(
    SenticGCNConfig,
    SenticGCNModel,
    SenticGCNEmbeddingConfig,
    SenticGCNEmbeddingModel,
    SenticGCNTokenizer,
    SenticGCNPreprocessor,
    SenticGCNPostprocessor,
    download_tokenizer_files,
)
import os
from typing import List 

# Note: If the relative filepaths are not working, try replacing them with the absolute filepaths to your module 
# The relative filepaths may be corrupted because it's calling a cached filepath


# Evaluates the words in one sentence 
class Evaluator:
    
    def __init__(self):
        print("Initiating model evaluator...")
        self.SENTENCE = "sentence"
        self.ASPECTS = "aspects"
        self.num_sentences = 1 
        
        # Initialize the tokenizer
        # print(os.getcwd())
        self.tokenizer = SenticGCNTokenizer.from_pretrained("./tokenizers/senticgcn/")
        
        # Obtaining the config variable for the MODEL
        self.config = SenticGCNConfig.from_pretrained(
            "./models/senticgcn/config.json"
        )

        # Obtaining the model itself 
        self.model = SenticGCNModel.from_pretrained(
            "./models/senticgcn/pytorch_model.bin",
            config=self.config
        )

        # Obtaining the config variable for the embedding model 
        self.embed_config = SenticGCNEmbeddingConfig.from_pretrained(
            "./embed_models/senticgcn_embed_semeval14_rest/config.json"
        )

        # Obtaining the embedding model itself 
        self.embed_model = SenticGCNEmbeddingModel.from_pretrained(
            "./embed_models/senticgcn_embed_semeval14_rest/pytorch_model.bin",
            config=self.embed_config
        )

        # Getting the preprocessor from everything 
        self.preprocessor = SenticGCNPreprocessor(
            tokenizer=self.tokenizer, embedding_model=self.embed_model,
            senticnet="./senticNet/senticnet.pickle",
            device="cpu")

        # Postprocessor for everything 
        self.postprocessor = SenticGCNPostprocessor()
          
    # Gather all results and return as array 
    def gather_results(self, sentence: str, words: List[str]):
        print(words)
        results = [0] * len(words) 
        print(results)
        for i, word in enumerate(words):
            if word is None:
                continue 
            results[i] = self._indiv_gather_results(sentence, word)
        print("Results:", results)
        return results 

    # Gets the evaluation result of a single word. Done so to prevent runtime error and to 
    # map each word to a result 
    def _indiv_gather_results(self, sentence: str, word: str):
        inputs = [{self.SENTENCE: sentence, self.ASPECTS: [word]}]
        try:
            # Run the model, get the result 
            processed_inputs, processed_indices = self.preprocessor(inputs)
            raw_outputs = self.model(processed_indices)
            post_outputs = self.postprocessor(processed_inputs=processed_inputs, model_outputs=raw_outputs)
            print(post_outputs)
            # Check for error 
            # Sample: {'sentence': ["India's", 'Adani', 'shares', 'see', 'extended', 'sell-off', 'as', 'credit', 'warnings', 'kick', 'in'], 'aspects': [[1]], 'labels': [-1]}
            return post_outputs[0]['labels'][0]
        except RuntimeError as e:
            print("An issue has occured:", e)
        
        # If got issue, return 0 (neutral)
        return 0
