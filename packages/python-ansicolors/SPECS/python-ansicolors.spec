%global pkgname ansicolors
%global desc Add ANSI colors and decorations to your strings.

Name:           python-%{pkgname}
Version:        1.1.8
Release:        13%{?dist}
Summary:        ANSI colors for Python

License:        ISC
URL:            https://pypi.python.org/pypi/ansicolors
Source0:        https://files.pythonhosted.org/packages/source/a/%{pkgname}/%{pkgname}-%{version}.zip

BuildArch:      noarch

# https://github.com/jonathaneunice/colors/pull/1
Patch0: add-bright-colors.patch

%description
%{desc}

%package -n python3-%{pkgname}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
%{desc}

%prep
%autosetup -n %{pkgname}-%{version} -p1

# Remove upstream egg-info
rm -rf %{pkgname}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=$(pwd) py.test-3 -v test

%files -n python3-%{pkgname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pkgname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/colors

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Sebastian Kisela <skisela@redhat.com> - 1.1.8-7
- Python 2 will be deprecated. Build python3 packages only.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-5
- Rebuilt for Python 3.7

* Fri Mar 23 2018 Sebastian Kisela <skisela@redhat.com> - 1.1.8-4
- Add option to use bright colors

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 skisela@redhat.com - 1.1.8-2
- Fix description macro. Reported at https://bugzilla.redhat.com/1498065.

* Fri Jul 14 2017 Sebastian Kisela <skisela@redhat.com> - 1.1.8-1
- Initial 1.1.8 package version
