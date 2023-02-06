import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import { POST_MODELRESULTS_URL } from './routes';
import cookie from 'js-cookie';
import Filesaver from 'file-saver';

class Storedpage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            spinCount: 0,
        };
        this.storedOutput = JSON.parse(sessionStorage.getItem("output"));
        console.log(this.storedOutput);
    }

    componentDidMount() {
        console.log(sessionStorage);
        this.storedOutput = JSON.parse(sessionStorage.getItem("output")) || []; // Stores as a list of 2 elements: key, value
        console.log(this.storedOutput);
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
            this.setState({ ...this.state, results: response.data.result, spinCount: 0 });
        }).catch(error => {
            console.log("ERROR AT GETTING RESULTS")
            console.log(error);
            this.setState({ spinCount: 0 })
        })
    }

    render() {

        const wordOutputs = Array.from({length: this.storedOutput.length}, (_, i) => {
            if (i % 3 == 0) {
                return (
                    <div className="center-container" style={{display: "flex", justifyContent: "center"}}>
                        {[i, i + 1, i + 2].map(e => 
                            ((e < this.storedOutput.length) && (
                                <div key={e} className="regular" style={{width: "24%", padding: "10px"}}>
                                    {console.log("Updating wordOutputs", e)}
                                    <label htmlFor={`input${i}`} className="regular label font-size-12">Word (or phrase) {e + 1}</label>
                                    <span key={e} id={`name${e}`} type="text" className="regular font-size-12" marginTop="5px">{this.storedOutput[e][0]}</span>
                                    <br />
                                    <span key={`result${e}`} id={`result${e}`} type="text" className="regular font-size-12 impt" marginTop="5px">{this.storedOutput[e][1]}</span>
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
                    <h1 class="center-container impt label">Financial Language Analyzer Storage</h1>
                    <div className="center-container">
                        <label className="regular label font-size-24 center-container">
                            Your previous outputs
                        </label>
                    </div>
                    <div>
                        {wordOutputs}
                    </div>
                    <div className="center-container">
                        {this.state.spinCount == 0 ? (
                            <button className="regular button center-container" style={{alignItems: "center", width: "200px"}} type="submit">DOWNLOAD</button>) : (
                                <button disabled className="regular button center-container" style={{alignItems: "center", width: "200px"}} type="submit">DOWNLOAD</button>
                            )}
                    </div>
                    <div className="center-container">
                        {this.state.spinCount == 1 && (
                            <h2 className="regular impt">Downloading...</h2>
                        )}
                    </div>
                    <div className="center-container">
                        <h4 className="regular">Download functionality coming soon! Return to <a href="/">computing outputs</a></h4>
                    </div>
                </form>
            </div>
        );
    }
}


console.log("Homepage Storedpage.js");
export default Storedpage;
