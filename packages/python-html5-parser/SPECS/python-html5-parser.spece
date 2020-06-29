%global srcname html5-parser

Name:           python-%{srcname}
Version:        0.4.9
Release:        2%{?dist}
Summary:        A fast, standards compliant, C based, HTML 5 parser for python

# html5-parser-0.4.4/gumbo/utf8.c is MIT
License:        ASL 2.0 and MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconf
# For tests
BuildRequires:  python3-lxml >= 3.8.0
BuildRequires:  gtest-devel
BuildRequires:  python3-chardet
BuildRequires:  python3-beautifulsoup4

%description
A fast, standards compliant, C based, HTML 5 parser for python

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

# This package bundles sigil-gumbo a fork of gumbo
# Base project: https://github.com/google/gumbo-parser
# Forked from above: https://github.com/Sigil-Ebook/sigil-gumbo
# It also patches that bundled copy with other changes.
# sigil-gumbo bundled here was added 20170601
Provides:      bundled(sigil-gumbo) = 0.9.3-20170601git0830e1145fe08
# sigil-gumbo forked off gumbo-parser at this commit in 20160216
Provides:      bundled(gumbo-parser) = 0.9.3-20160216git69b580ab4de04

%description -n python3-%{srcname}
A fast, standards compliant, C based, HTML 5 parser for python

%prep
export debug=True
%autosetup -n %{srcname}-%{version} -p1

# remove shebangs from library files
sed -i -e '/^#!\//, 1d' src/html5_parser/*.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.9-2
- Rebuilt for Python 3.9

* Sat Feb 15 2020 Kevin Fenzi <kevin@scrye.com> - 0.4.9-1
- Update to 0.4.9. Fixes bug 1768159

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.8-3
- Drop python2 subpackages and dependdencies. Fixes #1744402 and #1744646

* Tue Aug 20 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.8-2
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.8-1
- Update to latest version (#1742306)
- This fixes compatibility with python-beautifulsoup4 4.8.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.7-1
- Update to 0.4.7. Fixes bug #1716728

* Sat May 18 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.6-1
- Update to 0.4.6. Fixes bug #1709226

* Sun Apr 14 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.5-1
- Update to 0.4.5. Fixes bug #1697342

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.4-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 08 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.4-4
- Rebuild for upgrade path from f27

* Fri Oct 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.4-3
- Adjust BuildRequires names for older releases

* Fri Oct 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.4-2
- Clarify bundled copy of sigil-gumbo in spec comments.

* Sat Aug 12 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.4-1
- Initial version for Fedora
