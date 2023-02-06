import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import { POST_MODELRESULTS_URL } from './routes';
import cookie from 'js-cookie';
import Storedpage from './Storedpage';

class MainPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            sentence: '', 
            numWords: 1, 
            words: new Array(9).fill(null), 
            results: new Array(9).fill(null),
            spinCount: 0,  // Controlling whether eval button is interactable 

        };

        // Binding functions 
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        console.log("Event in handleChange:", event);
        console.log("Handling change: query is", event.target.value)
        this.setState({ sentence: event.target.value });
        console.log(this.state);
    }

    handleSubmit(event) {
        console.log("Event in handleSubmit:", event);
        event.preventDefault();
        const { sentence, numWords, words } = this.state;
        let submitWords = [...words];
        submitWords = submitWords.slice(0, numWords);
        console.log(sentence);
        console.log(words);
        console.log(submitWords);
        this.setState({ spinCount: 1 });
        // Send the query to the Django backend
        axios.post(`${POST_MODELRESULTS_URL}`, {
            sentence: sentence, 
            words: submitWords, 
        }, {
            headers: {
                'X-CSRFToken': cookie.get('csrftoken'), 
            }
        }).then(response => {
            console.log("GETTING RESULTS SUCCESS");
            console.log(response);
            console.log(response.data.result);
            // Update session storage 
            let curStored = JSON.parse(sessionStorage.getItem("output")) || [];
            for (let i in submitWords) {
                if (submitWords[i]) {
                    curStored.push([submitWords[i], response.data.result[i]]);
                }
            }
            sessionStorage.setItem("output", JSON.stringify(curStored));
            console.log(sessionStorage);
            this.setState({ ...this.state, results: response.data.result, spinCount: 0 });
        }).catch(error => {
            console.log("ERROR AT GETTING RESULTS")
            console.log(error);
            this.setState({ spinCount: 0 })
        })
    }

    // Update the number of words so we can have a dropdown for the number of words we need 
    handleNumberOfWordsChange = (event) => {
        console.log("Event in handleNumberOfWordsChange:", event);
        console.log("Handling number of words change: query is", event.target.value)
        this.setState({
            numWords: event.target.value, 
        });
        console.log(this.state);
    }

    // Handles the change of each word 
    // Need to edit it to set words 
    handleEachWordChange = (index, event) => {
        console.log("Event in handleEachWordChange:", event);
        console.log("Handling change: query is", event.target.value)
        console.log(this.state);
        const curWords = [...this.state.words]; 
        console.log("Curwords:", curWords);
        curWords[index] = event.target.value;
        this.setState({ words: curWords });
        console.log(this.state.words);
    }

    render() {

        // Need to find a way to submit 
        // This renders the inputOptions 3 in one row, side-by-side 
        const wordInputFields = Array.from({length: this.state.numWords}, (_, i) => {
            if (i % 3 == 0) {
                return (
                    <div className="center-container" style={{display: "flex", justifyContent: "center"}}>
                        {[i, i + 1, i + 2].map(e => 
                            ((e < this.state.numWords) && (
                                <div key={e} className="regular" style={{width: "24%", padding: "10px"}}>
                                    {console.log("Updating wordInputFields", e)}
                                    <label htmlFor={`input${i}`} className="regular label font-size-12">Word (or phrase) {e + 1}</label>
                                    <input 
                                        className="regular font-size-12"
                                        key={e} 
                                        id={`input${e}`} 
                                        type="text" 
                                        placeholder="Enter your word/phrase"
                                        value={this.state.words[e] || ''}
                                        onChange={(event) => this.handleEachWordChange(e, event)}
                                        />
                                    <br />
                                    <span key={e+9} id={`result${e}`} type="text" className="regular font-size-12 impt" marginTop="5px">{this.state.results[e]}</span>
                                </div>
                                )
                            )
                        )}
                    </div>
                )
            }
    })
        return (
            <div style={{display: "flex", alignItems: "center", justifyContent: "center", height: "100vh"}}>
                {console.log(this)}
                <form onSubmit={this.handleSubmit}>
                    <h1 className="center-container impt label">Financial Language Analyzer</h1>
                    <div className="center-container">
                        <label htmlFor="sentence" className="regular label font-size-24 center-container">
                            Enter any text you wish to evaluate: 
                        </label>
                        <textarea
                            className="regular label center-container"
                            style={{
                                width: "800px", 
                                height: "80px", 
                                fontSize: "16px", 
                                fontFamily: 'Montserrat', 
                            }}
                            type="text"
                            placeholder="Enter the sentence(s) you want to evaluate here"
                            value={this.state.query}
                            onChange={this.handleChange}
                        />
                    </div>
                    <label htmlFor="num-words" className="regular label center-container" style={{marginTop: "20px"}}>
                        Number of Entries
                        <br />
                        <select id="num-words" value={this.state.numWords} onChange={this.handleNumberOfWordsChange} style={{height: "20px", width: "50px"}}>
                            {Array.from({length: 9}, (_, i) => (
                                <option key={i+1} value={i+1} className="regular font-size-12">
                                    {i+1}
                                </option>
                            ))}
                        </select>
                    </label>
                    <div>
                        {wordInputFields}
                    </div>
                    <div className="center-container">
                        {this.state.spinCount == 0 ? (
                            <button className="regular button center-container" style={{alignItems: "center"}} type="submit">EVALUATE</button>) : (
                                <button disabled className="regular button center-container" style={{alignItems: "center"}} type="submit">EVALUATE</button>
                            )}
                    </div>
                    <div className="center-container">
                        {this.state.spinCount == 1 && (
                            <h2 className="regular impt">Evaluating...</h2>
                        )}
                    </div>
                    <div className="center-container">
                        <h4 className="regular">Coming soon: Past requests, parsing urls, stock recommendations. See your <a href="/stored">stored outputs</a></h4>
                    </div>
                </form>
            </div>
        );
    }
}


console.log("Homepage Mainpage.js");
export default MainPage;
