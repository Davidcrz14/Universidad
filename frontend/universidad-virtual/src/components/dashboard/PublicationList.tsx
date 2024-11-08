import React from 'react';
import { Publication } from '../../interfaces/institute';

interface PublicationListProps {
    publications: Publication[];
}

const PublicationList: React.FC<PublicationListProps> = ({ publications }) => {
    return (
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {publications.length === 0 ? (
                <p className="text-gray-500 text-center py-10 col-span-3">
                    No hay publicaciones disponibles
                </p>
            ) : (
                publications.map((pub) => (
                    <div key={pub.id} className="bg-white overflow-hidden shadow rounded-lg">
                        <div className="px-4 py-5 sm:p-6">
                            <div className="flex items-center justify-between">
                                <h3 className="text-lg leading-6 font-medium text-gray-900">
                                    {pub.title}
                                </h3>
                                <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                                    pub.type === 'noticia'
                                        ? 'bg-blue-100 text-blue-800'
                                        : 'bg-green-100 text-green-800'
                                }`}>
                                    {pub.type}
                                </span>
                            </div>
                            <p className="mt-1 max-w-2xl text-sm text-gray-500">
                                {new Date(pub.created_at).toLocaleDateString()}
                            </p>
                            <div className="mt-4 text-gray-700">
                                <p>{pub.content}</p>
                            </div>
                        </div>
                    </div>
                ))
            )}
        </div>
    );
};

export default PublicationList;
