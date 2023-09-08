import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./pages/Home"
import About from "./pages/About"
import CadastroTask from "./pages/CadastroTask"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/about" element={<About />}/>
        <Route path="/cadastro-task" element={<CadastroTask />}/>
      </Routes>
    </BrowserRouter>
  )
}