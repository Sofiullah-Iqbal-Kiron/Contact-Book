import SearchBar from "./SearchBar";
import ContactList from "./ContactList";

export default function SideBar() {
  return (
    <div className="bg-gray-50 px-2">
        <SearchBar/>
        <ContactList/>
    </div>
  )
}
