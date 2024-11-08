export interface Institute {
    id: number;
    name: string;
    description: string;
    created_at: string;
}

export interface Publication {
    id: number;
    title: string;
    content: string;
    type: 'noticia' | 'evento';
    institute: number;
    created_at: string;
    updated_at: string;
}
