import TopBar from "./components/TopBar";
import SideBar from "./components/SideBar";
import DetailsPanel from "./components/DetailsPanel";
import AddContactForm from "./components/AddContactForm/AddContactForm";
import TestUseFormContext from "./components/TestComponents/TestUseFormContext";
import TestUseFieldArray from "./components/TestComponents/TestUseFieldArray";

function App() {
  return (
    <div className="h-screen">
      {/* <TestUseFormContext /> */}
      <TestUseFieldArray />
      {/* <AddContactForm /> */}
      {/* <TopBar />
      <div className="flex bg-lime-300">
        <SideBar />
        <DetailsPanel />
      </div> */}
    </div>
  );
}

export default App;
