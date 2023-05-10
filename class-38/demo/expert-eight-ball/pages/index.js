import Head from 'next/head';
import Header from '../components/Header';
import QuestionForm from '../components/QuestionForm';
import EightBall from '../components/EightBall';
import Response from '../components/Response';
import Footer from '../components/Footer';
import { replies } from '../data';
import { useState } from 'react';


export default function Home() {
    // Initialize our array
    const [questions, setQuestions] = useState([]);
    // remove the reply because it was not necessary and we are tracking that with an answer below
    function handleQuestion(question) {
        // we need to add the question
        const randIndex = Math.floor(Math.random() * replies.length);
        const answer = replies[randIndex];
        const questionObj = {
            // This accounts for index starting at 0 and gives us a start point of 1
            id: questions.length + 1,
            question: question,
            answer: answer,
        };
        // Refactored names to be a little more clear and able to be understood.
        // Run this line below and ask chatgpt to explain it to you. Will make more sense.
        setQuestions([...questions, questionObj]);
    }

    function getAnswer() {
        if (questions.length === 0) {
            return "";
        } else {
            return questions[questions.length - 1].answer;
        }
    }

    return (
        <>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>
            <div className='space-y-8'>
                {/*passing in the array length for the question answered*/}
                <Header answerCount={questions.length} />
                <main>
                    <QuestionForm onQuestion={handleQuestion} />
                    <EightBall answer={getAnswer()} />
                    <Response questionList={questions} />
                </main>
                <Footer />
            </div>
        </>
    );
}











