import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./pages/Home"
import About from "./pages/About"
import CadastroTask from "./pages/CadastroTask"
import Navbar from "./components/Navbar"

export default function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto px-10">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />}/>
          <Route path="/about" element={<About />}/>
          <Route path="/tasks/:id" element={<CadastroTask />}/>
          <Route path="/cadastro-task" element={<CadastroTask />}/>
        </Routes>
      </div>
    </BrowserRouter>
  )
}
