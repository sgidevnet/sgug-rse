%global		oname Parsley
%global		lowname parsley

Name:		python-parsley
Version:	1.3
Release:	17%{?dist}
Summary:	Parsing and pattern matching made easy
License:	MIT
URL:		https://launchpad.net/parsley
Source0:	https://files.pythonhosted.org/packages/source/P/%{oname}/%{oname}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-twisted
BuildRequires:	python3-sphinx

%global _description\
A parser generator library based on OMeta, and other useful parsing tools.\
Parsley is a parsing library for people who find parsers scary or\
annoying. I wrote it because I wanted to parse a programming language,\
and tools like PLY or ANTLR or Bison were very hard to understand and\
integrate into my Python code. Most parser generators are based on LL\
or LR parsing algorithms that compile to big state machine\
tables. It was like I had to wake up a different section of my brain\
to understand or work on grammar rules.\
\
Parsley, like pyparsing and ZestyParser, uses the PEG algorithm, so\
each expression in the grammar rules works like a Python\
expression. In particular, alternatives are evaluated in order, unlike\
table-driven parsers such as yacc, bison or PLY.\
\
Parsley is an implementation of OMeta, an object-oriented\
pattern-matching language developed by Alessandro Warth at\
thesis, which provides a detailed description of OMeta:\
http://www.vpri.org/pdf/tr2008003_experimenting.pdf

%description %_description

%package -n python3-parsley
Summary: %summary
%{?python_provide:%python_provide python3-parsley}

%description -n python3-parsley %_description

%prep
%setup -q -n %{oname}-%{version}
rm -rf *.egg*

%build
%py3_build
make -C doc html man
rm -f doc/_build/html/.buildinfo

%install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{_builddir}/%{oname}-%{version}/doc/_build/man/%{lowname}.1* %{buildroot}%{_mandir}/man1

%check
# Exclude only test_vm_builder tests, as they are failing due to missing vm files.
py.test-%{python3_version} terml/test ometa/test --ignore=ometa/test/test_vm_builder.py

%files -n python3-parsley
%license LICENSE
%doc NEWS README
%{_mandir}/man1/%{lowname}.1*
%{python3_sitelib}/%{oname}-%{version}-py3.*.egg-info
%{python3_sitelib}/ometa/
%{python3_sitelib}/__pycache__/%{lowname}.*
%{python3_sitelib}/%{lowname}.*
%{python3_sitelib}/terml/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.3-12
- Fix BZ #1687413

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.3-7
- Provide a Python 3 subpackage (rhbz#1472491)
- Run tests

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-6
- Python 2 binary package renamed to python2-parsley
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Robert Mayr <robyduck@fedoraoproject.org> 1.3-1
- Bump release to 1.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Robert Mayr <robyduck@fedoraoproject.org> 1.2-3
- Applying permission fix and correct check section BZ #1179947

* Thu Jan 08 2015 Robert Mayr <robyduck@fedoraoproject.org> 1.2-2
- Applying bugfixes accordingly to comments in BZ #1179947

* Wed Jan 07 2015 Robert Mayr <robyduck@fedoraoproject.org> 1.2-1
- Initial package for Fedora
