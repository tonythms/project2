#include <cppunit/TestCase.h>
#include <cppunit/TestFixture.h>
#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/TestResult.h>
#include <cppunit/TestResultCollector.h>
#include <cppunit/TestRunner.h>
#include <cppunit/BriefTestProgressListener.h>
#include <cppunit/CompilerOutputter.h>
#include <cppunit/XmlOutputter.h>
#include <netinet/in.h>


#include <iostream>
#include <string>
#include <list>

#include "Calculator.hpp"

using CppUnit::TestFixture;
using std::cerr;

//-----------------------------------------------------------------------------

class TestCalculator : public CppUnit::TestFixture
{
    CPPUNIT_TEST_SUITE(TestCalculator);
    CPPUNIT_TEST(testSummation);
    CPPUNIT_TEST(testDifference);
    CPPUNIT_TEST(testMultiplication);
    CPPUNIT_TEST(testDivision);
    CPPUNIT_TEST_SUITE_END();

public:
    void setUp(void);
    void tearDown(void);

protected:
    void testSummation(void);
    void testDifference(void);
    void testMultiplication(void);
    void testDivision(void);

private:

    Calculator *mTestObj;
};

//-----------------------------------------------------------------------------

void
TestCalculator::testSummation(void)
{
    CPPUNIT_ASSERT(9 == mTestObj->Summation(6,3));
}

void
TestCalculator::testDifference(void)
{
    CPPUNIT_ASSERT(3 == mTestObj->Difference(6,3));
}

void
TestCalculator::testMultiplication(void)
{
    CPPUNIT_ASSERT(18 == mTestObj->Multiplication(6,3));
}

void
TestCalculator::testDivision(void)
{
    CPPUNIT_ASSERT(2 == mTestObj->Division(6,3));
}

void
TestCalculator::setUp(void)
{
    mTestObj = new Calculator();
}

void TestCalculator::tearDown(void)
{
    delete mTestObj;
}

//-----------------------------------------------------------------------------

CPPUNIT_TEST_SUITE_REGISTRATION( TestCalculator );

int main(int argc, char* argv[])
{
    // informs test-listener about testresults
    CPPUNIT_NS::TestResult testresult;

    // register listener for collecting the test-results
    CPPUNIT_NS::TestResultCollector collectedresults;
    testresult.addListener (&collectedresults);

    // register listener for per-test progress output
    CPPUNIT_NS::BriefTestProgressListener progress;
    testresult.addListener (&progress);

    // insert test-suite at test-runner by registry
    CPPUNIT_NS::TestRunner testrunner;
    testrunner.addTest (CPPUNIT_NS::TestFactoryRegistry::getRegistry().makeTest ());
    testrunner.run(testresult);

    // output results in compiler-format
    CPPUNIT_NS::CompilerOutputter compileroutputter(&collectedresults, std::cerr);
    compileroutputter.write ();

    // Output XML for Jenkins CPPunit plugin
    ofstream xmlFileOut("cppTestBasicMathResults.xml");
    XmlOutputter xmlOut(&collectedresults, xmlFileOut);
    xmlOut.write();

    // return 0 if tests were successful
    return collectedresults.wasSuccessful() ? 0 : 1;
}

