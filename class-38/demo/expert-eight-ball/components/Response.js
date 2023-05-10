export default function Response({ questionList: questions }) {

    if (questions.length == 0) {
        // not displaying the table until we have asked a question.
        return (
            <h2 className="w-1/2 mx-auto my-8 text-4xl text-center"> No questions have been asked! </h2>
        );

    } else {

        return (
            <table className="w-1/2 mx-auto my-4 border">
                <thead>
                    <tr>
                        <th className="border border-black">No.</th>
                        <th className="border border-black">Question</th>
                        <th className="border border-black">Response</th>
                    </tr>
                </thead>
                <tbody>
                    {/* mapping over the array and creating a new tr with td for each questions asked. */}
                    {questions.map(item => (
                        // This key is a requirement to use so JS knows what object it is working with?
                        <tr key={item.id}>
                            <td className="p-2 border border-black">{item.id}</td>
                            <td className="p-2 border border-black">{item.question}</td>
                            <td className="p-2 border border-black">{item.answer}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        );
    }
}
