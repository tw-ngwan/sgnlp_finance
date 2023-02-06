# Test file for training SGNLP Model. NOT TO BE USED (see worker.ipynb)

from sgnlp.models.sentic_gcn.train import SenticGCNTrainer, SenticGCNBertTrainer
from sgnlp.models.sentic_gcn.utils import parse_args_and_load_config, set_random_seed

cfg = parse_args_and_load_config(config_path="config/sentic_gcn_config.json")
if cfg.seed is not None:
    set_random_seed(cfg.seed)
trainer = SenticGCNTrainer(cfg) if cfg.model == "senticgcn" else SenticGCNBertTrainer(cfg)
trainer.train()

# Possible issue: I have no idea where my model is being saved to. I don't even think it's being saved since the folder is empty 
# https://sgnlp.aisingapore.net/docs/model/senticgcn.html apparently shows that you should have two pytorch_model.bin. So sth is wrong...

# You asked in the forums. See what they say