
import './App.css';

const App=()=> {
  const name="tina";
  const isNameShowing=!true;
  return (
    <div className="App">
      <h1>hello {isNameShowing?name: 'someone '} world</h1>
    </div>
  );
}

export default App;
