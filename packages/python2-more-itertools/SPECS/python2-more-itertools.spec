%global srcname more-itertools

Name:           python2-%{srcname}
Version:        5.0.0
Release:        2%{?dist}
Summary:        Python 2 version of more-itertools
License:        MIT
URL:            https://github.com/erikrose/more-itertools
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-six

# This is only used as a dependency of pytest
Provides:       deprecated()

%{?python_provide:%python_provide python2-%{srcname}} 

%description
Python''s itertools library is a gem - you can compose elegant solutions for
a variety of problems with the functions it provides. In more-itertools
we collect additional building blocks, recipes, and routines for working with
Python iterables.

Python 2 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py2_build

%install
%py2_install

# Don't ship the tests
rm -r %{buildroot}%{python2_sitelib}/more_itertools/tests

%check
%{__python2} setup.py test

%files
%license LICENSE
%doc README.rst PKG-INFO
%{python2_sitelib}/more_itertools/
%{python2_sitelib}/more_itertools-%{version}-py%{python2_version}.egg-info/


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-1
- Update to 5.0.0, the latest version that supports Python 2

* Tue May 21 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-6
- Fork from the python-more-itertools package (#1582171)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.7

* Tue May 22 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Backport upstream fix for Python 3.7

* Sat Mar 24 2018 Thomas Moschny <thomas.moschny@gmx.de> - 4.1.0-1
- Update to 4.1.0.
- Do not package tests.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 aarem AT fedoraproject DOT org - 2.3-1
- update to 2.3
* Fri Oct 14 2016 aarem AT fedoraproject DOT org - 2.2-4
- fixed missing sum in line 9 of spec file, per BZ #138195
* Sat Oct 8 2016 aarem AT fedoraproject DOT org - 2.2-3
- renamed spec file to match package as per BZ #1381029
-fixed bug (incorrect python3_provides) as per BZ #1381029
- use common macro for description as per suggestion in BZ #1381029

* Wed Oct 05 2016 aarem AT fedoraproject DOT org - 2.2-2
- separated python and python3 cases as per BZ #1381029

* Sun Oct 02 2016 aarem AT fedoraproject DOT org - 2.2-1
- initial packaging of 2.2 version
