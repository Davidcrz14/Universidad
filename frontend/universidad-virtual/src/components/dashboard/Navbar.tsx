import { ChevronDown, LogOut, Menu } from 'lucide-react'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Institute } from '../../interfaces/institute'
import { authService } from '../../services/authService'
import { Button } from '../ui/button'
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from '../ui/dropdown-menu'
import { Sheet, SheetContent, SheetTrigger } from '../ui/sheet'

interface NavbarProps {
    institutes: Institute[]
    selectedInstitute: Institute | null
    onInstituteChange: (institute: Institute) => void
}

export default function Navbar({ institutes, selectedInstitute, onInstituteChange }: NavbarProps) {
    const navigate = useNavigate()
    const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false)

    const handleLogout = async () => {
        await authService.logout()
        navigate('/login')
    }

    const filteredInstitutes = institutes.filter(institute =>
        institute.name.toLowerCase() !== "administracion" &&
        institute.name.toLowerCase() !== "administración"
    )

    return (
        <nav className="bg-indigo-600 text-white shadow-lg">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">
                    <div className="flex items-center">
                        <div className="flex-shrink-0">
                            <img className="h-8 w-8" src="/giphy.gif" alt="Logo" />
                        </div>
                        <div className="hidden md:block ml-10">
                            <DropdownMenu>
                                <DropdownMenuTrigger asChild>
                                    <Button variant="ghost" className="text-white hover:bg-indigo-500">
                                        {selectedInstitute ? selectedInstitute.name : 'Institutos'}
                                        <ChevronDown className="ml-2 h-4 w-4" />
                                    </Button>
                                </DropdownMenuTrigger>
                                <DropdownMenuContent>
                                    {filteredInstitutes.map((institute) => (
                                        <DropdownMenuItem
                                            key={institute.id}
                                            onClick={() => onInstituteChange(institute)}
                                            className="cursor-pointer"
                                        >
                                            {institute.name}
                                        </DropdownMenuItem>
                                    ))}
                                </DropdownMenuContent>
                            </DropdownMenu>
                        </div>
                    </div>
                    <div className="hidden md:block">
                        <Button
                            variant="ghost"
                            onClick={handleLogout}
                            className="text-white hover:bg-indigo-500"
                        >
                            <LogOut className="mr-2 h-4 w-4" />
                            Cerrar Sesión
                        </Button>
                    </div>
                    <div className="md:hidden">
                        <Sheet open={isMobileMenuOpen} onOpenChange={setIsMobileMenuOpen}>
                            <SheetTrigger asChild>
                                <Button variant="ghost" size="icon" className="text-white hover:bg-indigo-500">
                                    <Menu className="h-6 w-6" />
                                    <span className="sr-only">Abrir menú</span>
                                </Button>
                            </SheetTrigger>
                            <SheetContent side="right">
                                <nav className="flex flex-col gap-4 mt-6">
                                    <h2 className="text-lg font-semibold">Institutos</h2>
                                    {filteredInstitutes.map((institute) => (
                                        <Button
                                            key={institute.id}
                                            variant="ghost"
                                            className="justify-start"
                                            onClick={() => {
                                                onInstituteChange(institute)
                                                setIsMobileMenuOpen(false)
                                            }}
                                        >
                                            {institute.name}
                                        </Button>
                                    ))}
                                    <Button
                                        variant="ghost"
                                        onClick={handleLogout}
                                        className="justify-start"
                                    >
                                        <LogOut className="mr-2 h-4 w-4" />
                                        Cerrar Sesión
                                    </Button>
                                </nav>
                            </SheetContent>
                        </Sheet>
                    </div>
                </div>
            </div>
        </nav>
    )
}
