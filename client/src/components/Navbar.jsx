import React from "react";

export default function Navbar(props) {
  return (
    <nav
      className="navbar navbar-expand navbar-dark bg-dark"
      style={props.style}
    >
      <span className="navbar-brand mb-0">
        ReactDjango<b>TodoAPP</b>
      </span>
    </nav>
  );
}
