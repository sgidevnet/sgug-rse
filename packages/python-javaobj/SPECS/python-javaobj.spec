%global pypi_name javaobj

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Python module for serializing and deserializing Java objects

License:        ASL 2.0
URL:            https://github.com/tcalmant/python-javaobj
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz 
BuildArch:      noarch

%description
python-javaobj is a python library that provides functions for reading
and writing (writing is WIP currently) Java objects serialized or will
be deserialized by ObjectOutputStream. This form of object representation
is a standard data interchange format in Java world.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
# Deps for tests
BuildRequires:  maven-local
BuildRequires:  xorg-x11-server-Xvfb
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
python-javaobj is a python library that provides functions for reading
and writing (writing is WIP currently) Java objects serialized or will
be deserialized by ObjectOutputStream. This form of object representation
is a standard data interchange format in Java world.

%prep
%autosetup -n %{name}-%{version}
# Mock sth. for swing/awt
sed -i -e "s|'mvn'|'xvfb-run', 'xmvn', '-o'|" tests/tests.py
# Remove shebang
sed -i -e '/^#!\//, 1d' {javaobj/*.py,javaobj/v1/*.py,javaobj/v2/*.py}

%build
%py3_build

%install
%py3_install

%check
# https://github.com/tcalmant/python-javaobj/issues/37
#PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests/*.py
# Remove temporary builds
#rm -r java/target java/test*.ser

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream release 0.4.1 (rhbz#1825079)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0.1-1
- Remove Python 2 support
- Simplify spec file
- Update to latest upstream release 0.4.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20150606git64a6e0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Raphael Groner <projects.rg@smart.ms> - 0-0.7.20150606git64a6e0f
- Python3 support
- New upstream snapshot

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20131228gitb8ae821
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.5.20131228gitb8ae821
- Introduce license macro

* Tue Jan 06 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.4.20131228gitb8ae821
- BR python2

* Fri Dec 19 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.3.20142011svn31
- Use date of last commit (instead of checkout/export)
- Use GitHub (forked?)
- Remove sed fiddling
- Distribute tests folder as documentation samples

* Sat Nov 22 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.2.20142011svn31
- Fix swing/awt test

* Thu Nov 20 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.1.20142011svn31
- Initial
