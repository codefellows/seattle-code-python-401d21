import Link from 'next/link';

export default function Footer() {
    return (
        <footer className='flex items-center justify-between p-4 bg-gray-500 text-gray-50' >
            {/*Notice the import of the link above and the use of that in the routing to the new page.*/}
            <Link href={'/careers'}>
                <a className="px-3 py-2 bg-gray-700 rounded-lg">Careers</a>
            </Link>
            <p>Expert Eight Ball &copy;{ new Date().getFullYear() }</p>
        </footer>
    );
}
