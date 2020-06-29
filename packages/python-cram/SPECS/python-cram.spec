
%define srcname cram

Name:           python-cram
Version:        0.7
Release:        6%{?dist}
Summary:        Simple testing framework for command line applications
License:        GPLv2+
URL:            https://bitheap.org/cram/
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/pathfix.py
BuildRequires:  /usr/bin/pyflakes

%description
Cram tests look like snippets of interactive shell sessions. Cram runs each
command and compares the command output in the test with the command's actual
output.

%package -n python3-cram
Summary:        %{summary}
Requires:       python3

%description -n python3-cram
Cram tests look like snippets of interactive shell sessions. Cram runs each
command and compares the command output in the test with the command's actual
output.

%prep
%autosetup -n %{srcname}-%{version}

# Fix shebang - cram install adds -s so we avoid adding %%py3_shbang_opts here
pathfix.py -pni "%python3" scripts/cram

# remove shebangs
find . -type f -name '*.py' \
  -exec sed -i -e '/^#!/{1D}' {} \;

%build
%py3_build

%install
%py3_install

%check
# dist.t needs check-manifest which isn't packaged
# pep8.t needs pep8 which has been retired
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHON=%python3 scripts/cram -v tests

%files -n python3-%{srcname}
%doc NEWS.rst README.rst TODO.md
%license COPYING.txt

%{python3_sitelib}/*
%{_bindir}/cram

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Orion Poplawski <orion@nwra.com> - 0.7-4
- Fix cram shebang

* Fri Nov 22 2019 Orion Poplawski <orion@nwra.com> - 0.7-3
- Fix license (GPLv2+)

* Thu Nov 21 2019 Orion Poplawski <orion@nwra.com> - 0.7-2
- Run tests properly in mock

* Thu Nov 21 2019 Orion Poplawski <orion@nwra.com> - 0.7-1
- Update to 0.7

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6-18
- Subpackage python2-cram has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6-12
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-9
- Use %%{summary} macro in py2/py3 subpackages (thanks zbyszek@in.waw.pl)
  (rhbz#1179484)
- Drop old py3 minimum version numbers (thanks zbyszek@in.waw.pl)
  (rhbz#1179484)

* Mon Dec 07 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-8
- BR: python2-devel instead of python-devel (thanks zbyszek@in.waw.pl)
  (rhbz#1179484)
- rm Group tag from py3 subpackage (thanks zbyszek@in.waw.pl) (rhbz#1179484)
- Only package a single executable, /usr/bin/cram (thanks zbyszek@in.waw.pl)
  (rhbz#1179484)

* Sun Dec 06 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-7
- Correct Summary for python3-cram subpackage (thanks zbyszek@in.waw.pl)
  (rhbz#1179484)
- rm py3dir macro (thanks zbyszek@in.waw.pl) (rhbz#1179484)

* Sun Dec 06 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-6
- Update for latest Python packaging guidelines (thanks zbyszek@in.waw.pl)
  (rhbz#1179484)
- rm Group tag
- drop support for el6

* Sat Apr 04 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-5
- Use %%license macro (RHBZ #1179484)

* Thu Jan 08 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-4
- Correct License tag (RHBZ #1179484)

* Wed Jan 07 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-3
- Do not ship examples files in package. These are more like test files.
  (RHBZ #1179484)

* Tue Jan 06 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-2
- Fix bad copy-and-paste for %%description in python3 subpackage
- Fix shebangs to satisfy rpmlint's non-executable-script errors

* Tue Jan 06 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.6-1
- initial package
