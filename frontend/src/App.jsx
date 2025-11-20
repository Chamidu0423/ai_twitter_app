import {useState} from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [feedback, setFeedback] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePost = async () => {
    setLoading(true);
    setFeedback('null');

  try {
    const response = await fetch('http://127.0.0.1:8000/api/create_post/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({text: text}),
    });

    const data = await response.json();

    if (data.is_toxic) {
      setFeedback({type: 'error', message: data.message});
    } else {
      setFeedback({type: 'success', message: data.message});
      setText('');
    }
  } catch (error) {
    console.error('error:', error);
    setFeedback({type: 'error', message: 'Server error! Is backend running?'});
  }
  setLoading(false);
};

return (
  <div style = {{padding: '20px', fontFamily: 'Arial'}}>
    <h1>AI Twitter 🐦</h1>
    <textarea
      rows = "4"
      cols = "50"
      placeholder = "What's happening?"
      value = {text}
      onChange = {(e) => setText(e.target.value)}
      style = {{width: '100%', padding: '10px', fontSize: '16px'}}
      />
      <br /><br />

      <button
        onClick = {handlePost}
        disabled = {loading || !text}
        style = {{padding: '10px 20px', fontSize: '16px', cursor: 'pointer'}}
      >
        {loading ? "Checking...": "Post Tweet"}
      </button>

      {feedback && (
        <div style = {{
          marginTop: '20px',
          padding: '15px',
          borderRadius: '5px',
          color: 'white',
          backgroundColor: feedback.type === 'error' ? '#ff4444' : '#00C851'
        }}>
          <h3>{feedback.message}</h3>
        </div>
      )}    
  </div>
);
}

export default App;