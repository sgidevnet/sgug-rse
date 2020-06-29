%global srcname pwntools

Name:           python-%{srcname}
Version:        4.1.0
Release:        2%{?dist}
Summary:        A CTF framework and exploit development library

# Source contains four LICENSE*.txt files which explain the licenses which cover
# pwntools.
License:        MIT and BSD and GPLv2
URL:            https://github.com/Gallopsled/%{srcname}/
Source0:        https://github.com/Gallopsled/%{srcname}/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Waiting on pwntools to support newer sphinx shipped by Fedora.
# BuildRequires:  python3-sphinx

%description
Pwntools is a CTF framework and exploit development library. Written
in Python, it is designed for rapid prototyping and development, and
intended to make exploit writing as simple as possible.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       binutils

%description -n python3-%{srcname}
Pwntools is a CTF framework and exploit development library. Written
in Python, it is designed for rapid prototyping and development, and
intended to make exploit writing as simple as possible.

# Waiting on pwntools to support newer sphinx shipped by Fedora.
# %%package doc
# Summary:        pwntools documentation
#
# %%description doc
# Documentation for pwntools.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build
# Waiting on pwntools to support newer sphinx shipped by Fedora.
# # Generate html documentation.
# PYTHONPATH=${PWD} sphinx-build-2 docs/source html
# # Remove the sphinx-build leftovers.
# rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

rm -rf %{buildroot}%{python3_sitelib}/CHANGELOG.md
rm -rf %{buildroot}%{python3_sitelib}/CONTRIBUTING.md
rm -rf %{buildroot}%{python3_sitelib}/LICENSE-pwntools.txt
rm -rf %{buildroot}%{python3_sitelib}/README.md
rm -rf %{buildroot}%{python3_sitelib}/TESTING.md
rm -rf %{buildroot}%{python3_sitelib}/requirements.txt

%files -n python3-%{srcname}
%doc CHANGELOG.md CONTRIBUTING.md README.md TESTING.md requirements.txt
%license LICENSE-pwntools.txt
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pwn/
%{python3_sitelib}/pwnlib/
%{_bindir}/*

# Waiting on pwntools to support newer sphinx shipped by Fedora.
# %%files doc
# %%doc html
# %%license LICENSE-pwntools.txt

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.9

* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> - 4.1.0-1
- New upstream version

* Thu Dec 19 2019 W. Michael Petullo <mike@flyn.org> - 4.0.0-0.1.b0
- New upstream version
- Migrate to Python 3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 W. Michael Petullo <mike@flyn.org> - 3.12.2-1
- New upstream version
- Adjust requires.txt

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 W. Michael Petullo <mike@flyn.org> - 3.12.1-1
- New upstream version
- Drop python2-pypandoc requirement

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 W. Michael Petullo <mike@flyn.org> - 3.12.0-1
- Initial package
