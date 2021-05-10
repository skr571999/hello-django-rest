import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Navbar from "./components/Navbar";

function App() {
  return (
    <Router>
      <div>
        <Navbar style={{ height: "10vh" }} />
        <main
          className="container-fluid p-0 bg-primary"
          style={{ height: "90vh" }}
        >
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
          </Switch>
        </main>
      </div>
    </Router>
  );
}

export default App;
