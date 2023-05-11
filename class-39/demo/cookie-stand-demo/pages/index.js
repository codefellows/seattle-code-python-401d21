import Head from 'next/head';
import { useAuth } from "@/contexts/auth";

export default function Home() {

    // const user = null;
    // const user = {username: 'John'};
    const { user, login } = useAuth();
    return (
        <div>
            <Head>
                <title>Cookie Stand Demo</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                <button onClick={() => login('somebody', 'some-password')} className="p-2 text-white bg-gray-500 rounded">Login</button>
                {user ? (
                    <h2>Welcome {user.username}</h2>
                ) : (
                    <h2>Need to log in</h2>
                )}
            </main>
        </div>
    );
}
