%global srcname shamir-mnemonic

Name:    python-%{srcname}
Version: 0.1.0
Release: 3%{?dist}
Summary: Reference implementation of Shamir’s Secret-Sharing for Mnemonic Codes

License: MIT
URL:     https://github.com/trezor/python-shamir-mnemonic
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
This SLIP describes a standard and interoperable implementation of
Shamir’s secret sharing (SSS). SSS splits a secret into unique parts which can
be distributed among participants, and requires a specified minimum number of
parts to be supplied in order to reconstruct the original secret.
Knowledge of fewer than the required number of parts does not leak information
about the secret.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info/

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/shamir_mnemonic-*.egg-info/
%{python3_sitelib}/shamir_mnemonic/
%{_bindir}/shamir

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Jonny Heggheim <hegjon@gmail.com> - 0.1.0-1
- Inital packaging
