import TopBar from "./components/TopBar";
import SideBar from "./components/SideBar";
import DetailsPanel from "./components/DetailsPanel";

function App() {
  return (
    <div className="h-screen">
      <TopBar/>
      <div className="flex bg-lime-300">
        <SideBar/>
        <DetailsPanel/>
      </div>
    </div>
  )
}

export default App;
