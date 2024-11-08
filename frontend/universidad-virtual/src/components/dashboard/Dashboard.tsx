'use client'

import { Alert, AlertDescription, AlertTitle } from '../ui/alert'
import { Button } from '../ui/button'
import { Loader2 } from 'lucide-react'
import { useEffect, useState } from 'react'
import { Institute, Publication } from '../../interfaces/institute'
import { instituteService } from '../../services/instituteService'
import Navbar from './Navbar'
import PublicationList from './PublicationList'

export default function Dashboard() {
    const [institutes, setInstitutes] = useState<Institute[]>([])
    const [selectedInstitute, setSelectedInstitute] = useState<Institute | null>(null)
    const [publications, setPublications] = useState<Publication[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        fetchInitialData()
    }, [])

    const fetchInitialData = async () => {
        setLoading(true)
        setError(null)
        try {
            const institutesData = await instituteService.getAllInstitutes()
            setInstitutes(institutesData)

            const pubs = await instituteService.getPublications()
            setPublications(pubs)
        } catch (error) {
            console.error('Error fetching data:', error)
            setError('Error al cargar los datos iniciales. Por favor, intente de nuevo.')
        } finally {
            setLoading(false)
        }
    }

    const handleInstituteChange = async (institute: Institute) => {
        setLoading(true)
        setError(null)
        try {
            setSelectedInstitute(institute)
            const pubs = await instituteService.getPublications(institute.id)
            setPublications(pubs)
        } catch (error) {
            console.error('Error fetching publications:', error)
            setError(`Error al cargar las publicaciones de ${institute.name}. Por favor, intente de nuevo.`)
        } finally {
            setLoading(false)
        }
    }

    if (loading) {
        return (
            <div className="flex justify-center items-center h-screen bg-background">
                <Loader2 className="h-16 w-16 animate-spin text-primary" />
            </div>
        )
    }

    return (
        <div className="min-h-screen flex flex-col bg-background">
            <Navbar
                institutes={institutes}
                selectedInstitute={selectedInstitute}
                onInstituteChange={handleInstituteChange}
            />

            <main className="flex-1 w-full">
                <div className="container mx-auto px-4 py-6">
                    <h1 className="text-4xl font-extrabold text-foreground mb-8">
                        {selectedInstitute ? `Instituto de ${selectedInstitute.name}` : 'Administración de la UTM'}
                    </h1>

                    {error && (
                        <Alert variant="destructive" className="mb-6">
                            <AlertTitle>Error</AlertTitle>
                            <AlertDescription>{error}</AlertDescription>
                        </Alert>
                    )}

                    <div className="grid gap-6">
                        {publications.length > 0 ? (
                            <PublicationList publications={publications} />
                        ) : (
                            <div className="text-center py-12 bg-card rounded-lg shadow">
                                <p className="text-xl text-muted-foreground mb-4">
                                    No hay publicaciones disponibles.
                                </p>
                                <Button onClick={() => fetchInitialData()}>
                                    Recargar datos
                                </Button>
                            </div>
                        )}
                    </div>
                </div>
            </main>
        </div>
    )
}
