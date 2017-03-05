import pytest


def test_expect_keys(should):
    {'foo': 'bar'} | should.have.key('foo')
    {'foo': 'bar'} | should.have.key('foo') > should.be.equal.to('bar')
    'bar' | should.be.equal.to('bar')

    should({'foo': 'bar'}).have.key('foo') > should.be.equal.to('bar')
    should({'foo': 'bar'}).have.key('foo').which.should.be.equal.to('bar')

    with pytest.raises(AssertionError):
        {'foo': 'bar'} | should.have.key('bar')

    with pytest.raises(AssertionError):
        [] | should.have.key('bar')

    with pytest.raises(AssertionError):
        should({'foo': 'bar'}).have.key('foo') > should.be.equal.to('foo')

    with pytest.raises(AssertionError):
        should({'foo': 'bar'}).have.key('foo').which.should.be.equal.to('pepe')
