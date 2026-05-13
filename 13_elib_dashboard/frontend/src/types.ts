export interface Author {
    id: string;
    name: string;
}

export interface Book {
    id: string;
    title: string;
    description: string;
    coverImage: string;
    file: string;
    genre: string;
    created_at: string;
    author: Author;
}