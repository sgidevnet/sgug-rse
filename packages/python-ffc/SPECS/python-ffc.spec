Name:           python-ffc
Version:        2019.1.0.post0
%global fenics_version 2019.1
Release:        3%{?dist}
Summary:        Compiler for finite element variational forms

License:        LGPLv3+
URL:            https://fenics-ffc.readthedocs.org/
Source0:        https://bitbucket.org/fenics-project/ffc/downloads/ffc-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/ffc/downloads/ffc-%{version}.tar.gz.asc
Source2:        3083BE4C722232E28AD0828CBED06106DD22BAB3.gpg

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(fenics-fiat) >= %{fenics_version}
BuildRequires:  python3dist(fenics-ufl) >= %{fenics_version}
BuildRequires:  python3dist(fenics-dijitso) >= %{fenics_version}
BuildRequires:  cmake
BuildRequires:  gnupg2
# Note: a copy of gtest is bundled and used for tests during build. It
# could be unbundled, but I don't think this is worth the trouble in
# this case.

%global _description %{expand:
The FEniCS Form Compiler FFC is a compiler for finite element
variational forms, translating high-level mathematical descriptions of
variational forms into efficient low-level C++ code for finite element
assembly.}

%description %_description

%package -n python3-ffc
Summary: %summary
%{?python_provides python3-ffc}

%description -n python3-ffc %_description

%prep
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%autosetup -n ffc-%{version} -p1

sed -r -i '1d' ffc/__main__.py ffc/main.py

%build
%py3_build

%install
%py3_install

%check
# test_evaluate.py uses libs/ffc-factory, which is currently ignored
%__python3 -m pytest -v test/ --ignore=test/unit/ufc/finite_element/test_evaluate.py

%files -n python3-ffc
%license COPYING COPYING.LESSER
%doc README.rst ChangeLog.rst AUTHORS
%doc demo
/usr/bin/ffc
/usr/bin/ffc-3
%{python3_sitelib}/ffc
%{python3_sitelib}/fenics_ffc-%{version}-py%{python3_version}.egg-info/
%{_mandir}/man1/ffc.1*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1.0.post0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0.post0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2019.1.0.post0-1
- Initial packaging
