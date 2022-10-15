import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
// import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer'
import SignUp from './components/register';
import SignIn from './components/login';
import Logout from './components/logout';





const root = ReactDOM.createRoot(document.getElementById('root'));

const routing = (
  <Router>
    <React.StrictMode>
      <Header />
      <Routes>
        <Route exact path="/" element={<App />} />
        <Route path="register/" element={<SignUp />}/>
        <Route path="login/" element={<SignIn />}/>
        <Route path="logout/" element={<Logout />}/>
      </Routes>
      <Footer />
    </React.StrictMode>
  </Router>

);

root.render(routing)

// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
