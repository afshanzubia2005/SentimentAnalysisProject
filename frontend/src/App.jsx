import { useState } from 'react'
import hongjoong from './assets/hongjoong.png'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="hongjoong_image">
        <img src={hongjoong} className="honjoong" alt="hongjoong_image" />
      </div>
      <h1>Social Media Aggregator + Sentiment Analysis</h1>
      <h2>Enter a celebrity name to get all their latest juicy gossip!</h2>
      <div>the LLM will collect info on what ppl say abt them on social media
        + display it here
      </div>
      <textarea name="celebrityName"/>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          get the world's current opinion
        </button>
      </div>
      <p className="details">
        This is a project im building with React frontend + Flask backend. 
      </p>
    </>
  )
}

export default App
