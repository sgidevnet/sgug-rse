%global pkgname babelfish

Name:           python-%{pkgname}
Version:        0.5.5
Release:        19%{?dist}
Summary:        Python library to work with countries and languages

License:        BSD
URL:            https://babelfish.readthedocs.org/
Source:         https://github.com/Diaoul/%{pkgname}/archive/%{version}.tar.gz
Patch0:         python-babelfish-0.5.5-add_python39_support.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

%description
Babelfish makes it easy to work with countries, languages, scripts, ISO codes
and IETF codes from Python. It has converters between all different data
can be extended to use custom converters and data.

%package -n python3-%{pkgname}
Summary:        Python library to work with countries and languages
%{?python_provide:%python_provide python3-%{pkgname}}
Suggests:       %{name}-doc = %{version}-%{release}

%description -n python3-%{pkgname}
Babelfish makes it easy to work with countries, languages, scripts, ISO codes
and IETF codes from Python. It has converters between all different data
can be extended to use custom converters and data.

%package doc
Summary:        Documentation for %{pkgname} python library

%description doc
Documentation for %{pkgname} python library

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
%py3_build
pushd docs
%make_build text
%make_build man
find . -type f -name '.buildinfo' -delete
popd

%install
%py3_install
install -D -m 0644 docs/_build/man/%{pkgname}.1 %{buildroot}%{_mandir}/man1/%{pkgname}.1
chmod 755 %{buildroot}%{python3_sitelib}/%{pkgname}/tests.py
sed -i -e 's,^#!/usr/bin/env python$,#!/usr/bin/python3,g' %{buildroot}%{python3_sitelib}/%{pkgname}/tests.py

%check
%{__python3} setup.py test

%files -n python3-%{pkgname}
%license LICENSE
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/%{pkgname}-%{version}-py*.egg-info

%files doc
%doc AUTHORS README.rst HISTORY.rst docs/_build/text
%license LICENSE
%{_mandir}/man1/%{pkgname}.1*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0.5.5-17
- Add patch for Python 3.9 support

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-12
- Subpackage python2-babelfish has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-10
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.5-6
- Python3 changes

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 11 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.5-2
- LICENSE in doc subpackage
- Make test.py executable

* Wed Jan 13 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.5-1
- Initial package
