Name:           python-gitapi
Version:        1.1.0
Release:        0.a3%{?dist}.17
Summary:        Pure-Python API to git, which uses the command-line interface

License:        MIT
URL:            https://bitbucket.org/haard/gitapi
Source0:        https://pypi.python.org/packages/source/g/gitapi/gitapi-%{version}a2.tar.gz
# Ask upstream to include license in a separate file here:
# https://bitbucket.org/haard/gitapi/issue/3/include-the-license-in-a-separate-file
Source1:        LICENSE

BuildArch:      noarch
BuildRequires:  git

%global _description\
Pure-Python API to git, which uses the command-line interface.

%description %_description

%package -n     python3-gitapi
Summary:        Pure-Python API to git, which uses the command-line interface
%{?python_provide:%python_provide python3-gitapi}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       git

%description -n python3-gitapi
Pure-Python API to git, which uses the command-line interface.


%prep
%setup -q -n gitapi-%{version}a2
cp %{SOURCE1} .
# Remove egg
rm -r gitapi.egg-info
# Apply patches
sed -i 's/\r$//' gitapi/testgitapi.py
# Correct end of line encoding for README.rst
sed -i 's/\r$//' README.rst


%build
%py3_build


%install
%py3_install


%files -n python3-gitapi
%license LICENSE
%doc README.rst
%{python3_sitelib}/gitapi-%{version}a2-py%{python3_version}.egg-info/
%{python3_sitelib}/gitapi/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-0.a3.17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.a3.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-0.a3.15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-0.a3.14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.a3.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.a3.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-0.a3.11
- Remove Python 2 subpackage (#1627306)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.a3.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-0.a3.9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.a3.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.0-0.a3.7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-0.a3.6
- Python 2 binary package renamed to python2-gitapi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.a3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.a3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-0.a3.3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.a3.2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.a3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 1.1.0-0.a3
- Rebuilt for python 3.5

* Fri Jun 19 2015 Julien Enselme <jujens@jujens.eu> - 1.1.0-0.a2
- Update to 1.1.0a2
- Reformat BuildRequires
- Remove tests (cannot pass any more)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Julien Enselme <jujens@jujens.eu> - 1.0.1-1
- Update to 1.0.1

* Mon Oct 27 2014 Julien Enselme <jujens@jujens.eu> - 1.0.0-5
- Add license as source and not as patch.
- Use %%{version} tag in patch.

* Fri Aug 29 2014 Julien Enselme <jujens@jujens.eu> - 1.0.0-4
- Fix the wrong-file-end-of-line-encoding error in README.rst.
- Fix the summary-not-capitalized error.
- Add the license file.

* Thu Aug 14 2014 Julien Enselme <jujens@jujens.eu> - 1.0.0-3
- Don't duplicate the BR of gitapi.
- Remove egg-info from upstream.

* Thu Aug 14 2014 Julien Enselme <jujens@jujens.eu> - 1.0.0-2
- Add git as a BuildRequires. The git command is required to complete the tests.
- Add patch1 to configure author in the git repos to avoid the 'Please tell me who you are.' git error.

* Sun Aug 03 2014 Julien Enselme <jujens@jujens.eu> - 1.0.0-1
- Initial packaging.
