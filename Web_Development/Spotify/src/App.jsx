import React,{Component} from "react";
import Comp1 from "./components/Comp1";
import Comp2 from "./components/Comp2";
import Comp3 from "./components/Comp3";
import Comp4 from "./components/Comp4";
class App extends Component{
    
    render(){
        return <div id = "main">
        <div id="left">
           <Comp1></Comp1>
            <Comp2></Comp2>
        </div>
            <Comp3></Comp3>
            <Comp4></Comp4>
        </div>
    }
}
export default App;