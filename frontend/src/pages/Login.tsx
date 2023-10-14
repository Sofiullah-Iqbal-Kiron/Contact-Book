import { Button, TextField } from "@mui/material";
import Typography from "@mui/material/Typography";

export default function Login() {
  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gradient-to-r from-slate-300 to-violet-300">
        <h1 className="text-4xl font-semibold mb-5">
            Login
        </h1>
        <form className="flex flex-col w-1/2 space-y-8 ">
            <TextField label="User name" variant="standard"/>
            <TextField type="password" label="Password" variant="standard"/>
            <Button type="submit" variant="contained" color="secondary" size="small">Login</Button>
        </form>
    </div>
  )
}
