import { Button } from "@mui/material";
import TextField from "@mui/material/TextField";
import SearchIcon from '@mui/icons-material/Search';

export default function SearchBar() {
  return (
    <form className="flex space-x-2 justify-center items-center py-2">
      <input type="text" placeholder="search contact" className="input-field" />
      {/* <TextField placeholder="search contact" variant="outlined" size="small" color="info"/> */}
      <Button type="submit" variant="contained">
        <SearchIcon/>
      </Button>
    </form>
  );
}
