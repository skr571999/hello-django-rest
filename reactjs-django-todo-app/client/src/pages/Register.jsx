import React, { useState } from "react";
import { Link } from "react-router-dom";

export default function Register() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(username, email, password);
  };

  const handleReset = (e) => {
    setUsername("");
    setEmail("");
    setPassword("");
  };

  return (
    <div className="row justify-content-center m-0 p-0">
      <div className="col-10 col-md-8 py-4 row justify-content-center bg-white mt-4 rounded">
        <div className="col-12 text-center">
          <h3>Register, here</h3>
        </div>
        <form
          onSubmit={handleSubmit}
          onReset={handleReset}
          className="mt-4 col-12 col-md-10 col-lg-7"
        >
          <div className="form-group row align-items-center">
            <label
              htmlFor="username"
              className="pl-0 col-4 m-0 font-weight-bold"
            >
              Username
            </label>
            <input
              type="text"
              id="username"
              className="form-control col-8"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="form-group row align-items-center">
            <label htmlFor="email" className="pl-0 col-4 m-0 font-weight-bold">
              Email
            </label>
            <input
              type="email"
              id="email"
              className="form-control col-8"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="form-group row align-items-center">
            <label
              htmlFor="password"
              className="pl-0 col-4 m-0 font-weight-bold"
            >
              Password
            </label>
            <input
              type="password"
              id="password"
              className="form-control col-8"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="form-group row align-items-center justify-content-around mt-5">
            <button className="btn btn-outline-secondary" type="reset">
              Reset
            </button>
            <button className="btn btn-outline-success" type="submit">
              Submit
            </button>
          </div>
        </form>
        <div className="col-12 text-center">
          <p>
            Already have a account, <Link to="/login">Login here</Link>{" "}
          </p>
        </div>
      </div>
    </div>
  );
}
