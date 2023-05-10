export default function Header({ answerCount }) {
    return (
        <header className="flex items-center justify-between p-4 font-sans bg-gray-500 text-gray-50">
            <h1 className="text-4xl">Expert Eight Ball</h1>
            {/*grabbing answer count from it being passed in from index.js*/}
            <p>{answerCount} questions answered</p>
        </header>
    );
}
