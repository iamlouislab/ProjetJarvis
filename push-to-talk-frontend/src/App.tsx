import { useRef, useState } from "react";
import viteLogo from "/vite.svg";
import "./App.css";

import { AudioRecorder, useAudioRecorder } from "react-audio-voice-recorder";

function App() {
  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
      </div>
      <h1>Jarvis</h1>
      <div className="card">
        <PushToTalkButton />
        <p>
          Click on the button, talk and release the button to talk to Jarvis
        </p>
      </div>
    </>
  );
}

const PushToTalkButton = () => {
  const recorderControls = useAudioRecorder();
  const [recording, setRecording] = useState<Blob | null>(null);

  const addAudioElement = (blob: Blob) => {
    console.log("add audioelement");
    setRecording(blob);
  };

  const sendRecording = () => {
    // send recording to backend
    console.log(recording);
    const formData = new FormData();
    formData.append("file", recording as Blob);
    const res = fetch("http://127.0.0.1:5000/voice_path_input_callback", {
      // const res = fetch("http://localhost:3000", {
      method: "POST",
      body: formData,
    });
    console.log(res);
    setRecording(null);
  };

  return (
    <div className="flex flex-row gap-2 items-center">
      <AudioRecorder
        onRecordingComplete={(blob) => addAudioElement(blob)}
        recorderControls={recorderControls}
      />
      <button onClick={sendRecording} disabled={recording === null}>
        Send recording
      </button>
    </div>
  );
};

export default App;
