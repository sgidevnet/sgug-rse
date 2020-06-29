%global srcname guessit

Name:           python-%{srcname}
Version:        3.1.1
Release:        2%{?dist}
Summary:        Library to extract as much information as possible from a video filename
License:        LGPLv3
URL:            https://guessit.readthedocs.org/
Source:         https://github.com/guessit-io/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
# Doc building
BuildRequires:  python3-sphinx
BuildRequires:  python3-rebulk
BuildRequires:  python3-babelfish
BuildRequires:  python3-dateutil
# Tests
BuildRequires:  python3-pytest >= 3.3
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-PyYAML
BuildRequires:  mailcap

%global _description\
GuessIt is a python library that extracts as much information as possible from\
a video filename.\
\
It has a very powerful matcher that allows to guess properties from a video\
using its filename only. This matcher works with both movies and TV shows\
episodes.

%description %_description

%package -n python3-%{srcname}
Summary:        %summary
%{?python_provide:%python_provide python3-%{srcname}}
Suggests:       %{name}-doc = %{version}-%{release}

%description -n python3-%{srcname} %_description

%package doc
Summary:        Documentation for %{srcname} python library

%description doc %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
pushd docs
PYTHONPATH='..' %make_build text
PYTHONPATH='..' %make_build man
PYTHONPATH='..' %make_build html
find . -name .buildinfo -delete
popd

%install
%py3_install
# Remove shebang from Python3 libraries
for lib in `find %{buildroot}%{python3_sitelib} -name "*.py"`; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
install -D -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%files doc
%doc README.rst HISTORY.rst AUTHORS.rst CONTRIBUTING.rst docs/_build/text docs/_build/html
%license LICENSE
%{_mandir}/man1/%{srcname}.1*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 3.1.1-1
- Version 3.1.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Juan Orti Alcaine <jortialc@redhat.com> - 3.1.0-2
- Use automatic dependencies

* Tue Sep 03 2019 Juan Orti Alcaine <jortialc@redhat.com> - 3.1.0-1
- Version 3.1.0
- Enable tests

* Sun Sep 01 2019 Juan Orti Alcaine <jortialc@redhat.com> - 3.0.5-1
- Version 3.0.5

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-9
- Subpackage python2-guessit has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.4-5
- Install license in doc

* Thu Aug 31 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.4-4
- Disable the tests
- Build HTML docs
- Reduce summary lenght
- Remove shebangs from libraries

* Wed Aug 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.4-3
- Add BR needed to run tests
- Use an easier Source URL

* Tue Aug 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.4-2
- Add BR: python2-dateutil

* Mon Aug 28 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.4-1
- Initial package
