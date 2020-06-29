%global srcname scripttester

Name:           python-%{srcname}
Version:        0.1
Release:        8%{?dist}
Summary:        Utility for testing command line scripts

License:        BSD
URL:            https://pypi.org/project/scripttester/
Source0:        https://github.com/matthew-brett/scripttester/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%global desc %{expand:
Provides a class to be instantiated in tests that checks that scripts
can be run and give correct output.  The class tries to find your
scripts whether you have installed them or not.  If you have not
installed them, the scripts will not be on your system PATH, and we have
to find them.  The heuristic is to look (by default) in the directory
containing mymodule; if there is a setup.py file there, and a scripts
subdirectory, assume that directory contains the scripts.

Note there is no way of using this not-installed mechanism to find
entrypoint scripts, that have not been installed.  To find these, we
would have to run the setup.py file.}

%description
%{desc}

%package     -n python3-%{srcname}
Summary:        Utility for testing command line scripts

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
rst2html --no-datestamp README.rst README.html

# Documentation build
sed -i 's/python -msphinx/sphinx-build/' doc/Makefile
make -C doc html
rm -f doc/_build/html/.{buildinfo,nojekyll}

%install
%py3_install

%check
export PYTHONPATH=$PWD/build/lib
pytest-%{python3_version}

%files -n python3-%{srcname}
%license LICENSE
%doc README.html doc/_build/html
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Jerry James <loganjerry@gmail.com> - 0.1-2
- Drop python2 subpackage (bz 1651179)

* Wed Sep  5 2018 Jerry James <loganjerry@gmail.com> - 0.1-1
- Initial RPM
