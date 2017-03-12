# NOTE: functionality included in pytest 2.8.0
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# py.test tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest-cache module: working with cross-testrun state
Summary(pl.UTF-8):	Moduł pytest-cache - praca ze stanem pomiędzy uruchomieniami testów
Name:		python-pytest-cache
Version:	1.0
Release:	0.1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pytest-cache
Source0:	https://pypi.python.org/packages/source/p/pytest-cache/pytest-cache-%{version}.tar.gz
# Source0-md5:	e51ff62fec70a1fd456d975ce47977cd
URL:		http://bitbucket.org/hpk42/pytest-cache/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-execnet >= 1.1
BuildRequires:	python-pytest >= 2.2
BuildRequires:	python-pytest < 2.8
BuildRequires:	python-pytest-xdist
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-execnet >= 1.1
BuildRequires:	python3-pytest >= 2.2
BuildRequires:	python3-pytest < 2.8
BuildRequires:	python3-pytest-xdist
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
Requires:	python-pytest < 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-cache module: working with cross-testrun state.

%description -l pl.UTF-8
Moduł pytest-cache - praca ze stanem pomiędzy uruchomieniami testów.

%package -n python3-pytest-cache
Summary:	pytest-cache module: working with cross-testrun state
Summary(pl.UTF-8):	Moduł pytest-cache - praca ze stanem pomiędzy uruchomieniami testów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-pytest < 2.8

%description -n python3-pytest-cache
pytest-cache module: working with cross-testrun state.

%description -n python3-pytest-cache -l pl.UTF-8
Moduł pytest-cache - praca ze stanem pomiędzy uruchomieniami testów.

%package apidocs
Summary:	Documentation for pytest-cache module
Summary(pl.UTF-8):	Dokumentacja modułu pytest-cache
Group:		Documentation

%description apidocs
Documentation for pytest-cache module.

%description apidocs -l pl.UTF-8
Dokumentacja modułu pytest-cache.

%prep
%setup -q -n pytest-cache-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) PYTEST_PLUGINS=pytest_cache %{__python} -m pytest
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) PYTEST_PLUGINS=pytest_cache %{__python3} -m pytest
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst
%{py_sitescriptdir}/pytest_cache.py[co]
%{py_sitescriptdir}/pytest_cache-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-cache
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst
%{py3_sitescriptdir}/pytest_cache.py
%{py3_sitescriptdir}/__pycache__/pytest_cache.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_cache-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
