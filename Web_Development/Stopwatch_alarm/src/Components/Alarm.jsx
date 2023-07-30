import {useEffect,useRef,useState} from "react";
import mysong from "../assets/song.mp3"
const Alarm = ()=>{
    const time = new Date();
    const [chk,setChk] = useState(0);
    const [syssec,setSyssec] = useState("-");
    const [sysmin,setSysmin] = useState("-");
    const [syshrs,setSyshrs] = useState("-");
    const [userhr,setUserhr] = useState(null);
    const [usermin,setUsermin] = useState(null);
    const [usersec,setUsersec] = useState(null);
    const [showtime,setShowtime] = useState("")
    const audioRef = useRef();
    const hrref = useRef();
    const minref = useRef();
    const secref = useRef();
    
    useEffect(()=>{
        setInterval(()=>{
            setChk(()=>chk+1)
            setSyssec(Number(time.getSeconds()))
            setSysmin(Number(time.getMinutes()))
            setSyshrs(Number(time.getHours()))
        },1000) })
   
    useEffect(()=>{
        
        if(userhr === syshrs && usermin === sysmin && usersec === syssec){
            audioRef.current.play();
        }
    },[syshrs,sysmin,syssec,userhr,usermin,usersec])

    const setAlarm = (e) =>{
        e.preventDefault();
        
        setUserhr(Number(hrref.current.value));
        setUsermin(Number(minref.current.value));
        setUsersec(Number(secref.current.value)); 
        
        setShowtime("Set on "+hrref.current.value+" hours "+minref.current.value+" minutes "+ secref.current.value+" seconds")    
        
    }
  
    const stopAlarm = (e) =>{
        e.preventDefault();
        audioRef.current.pause();
        hrref.current.value = null;
        minref.current.value = null;
        secref.current.value = null;
        setUserhr(null);
        setUsermin(null);
        setUsersec(null);
        setShowtime("");
        
    }

    return (
        <div className="alamain">
            <div className="name">Alarm Clock</div>
            <div className="tym">
                <span id="hhrs">{syshrs}</span><span>:</span><span id="mmin">{(sysmin<10)?"0"+sysmin:sysmin}</span><span>:</span><span id="ssec">{(syssec<10)?"0"+syssec:syssec}</span></div>
            <div className="alrmset">
                <form className="form" >
                    <input type="number" placeholder="Enter hours (System format)" ref={hrref} />
                    <input type="number" placeholder="Enter minutes " ref = {minref}/>
                    <input type="number" placeholder="Enter seconds" ref = {secref}/>
                    <div className="butt" id="alabutt">
                        <button onClick={setAlarm} ><abbr title="Set alarm">Set</abbr></button>
                        <button onClick={stopAlarm}><abbr title="Stop and reset alarm">Stop</abbr></button>
                    </div>
                    <audio ref={audioRef} src = {mysong}></audio>
                </form>
                <div className="name" id="set">{showtime}</div>
            </div>
        </div>
    )
}
export default Alarm;                                                                                             