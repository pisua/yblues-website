import logo from './logo.svg';
import './App.css';
import { FormGenerator } from './components/formGenerator.js';
import ReactDOM from "react-dom";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useLocation
} from "react-router-dom";

function App() {
  return (
     <Router>
          <Routes>
            <Route path="/" exact component={FormGenerator} />
          </Routes>
      </Router>
  );
}

export default App;
