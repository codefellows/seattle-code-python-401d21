import Head from 'next/head';

export default function Home() {
    function questionAskedHandler(event) {
        event.preventDefault();
        alert(event.target.question.value);
    }
    return (
        <>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>
            <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
                <h1 className="text-4xl">Magic 8 Ball</h1>
                <p>1 questions answered</p>
            </header>
            <main>
                <form className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
                    <input name="question" className="flex-auto pl-1"/>
                    <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
                </form>
                <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
                    <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                        <p className="text-xl text-center">Ask me anything</p>
                    </div>
                </div>
            </main>
            <footer className="p-4 bg-gray-500 text-gray-50">
                <nav>
                    <a href='careers'>Careers</a>
                </nav>
            </footer>
        </>
    );
}
