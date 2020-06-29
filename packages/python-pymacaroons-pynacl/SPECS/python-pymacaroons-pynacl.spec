%{?python_enable_dependency_generator}
%global pkgname pymacaroons-pynacl

%global desc This is a Python re-implementation of the libmacaroons C library.\
Macaroons, like cookies, are a form of bearer credential. Unlike\
opaque tokens, macaroons embed caveats that define specific authorization\
requirements for the target service, the service that issued the root macaroon\
and which is capable of verifying the integrity of macaroons it receives.\
\
Macaroons allow for delegation and attenuation of authorization. They are\
simple and fast to verify, and decouple authorization policy from the\
enforcement of that policy.\


Name:           python-%{pkgname}
Version:        0.13.0
Release:        6%{?dist}
Summary:        Library providing non-opaque cookies for authorization

License:        MIT
URL:            https://github.com/ecordell/pymacaroons
Source0:        %{url}/archive/v%{version}/pymacaroons-v%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
%{desc}


%package doc
Summary: Documentation for python-pymacaroons-pynacl
BuildRequires:  python3-sphinx

%description doc
Documentation for the python-pymacaroons-pynacl package.

%{desc}


%prep
%autosetup -n pymacaroons-%{version}


%build
%py3_build

make %{?_smp_mflags} -C docs SPHINXBUILD=sphinx-build-3 html PYTHONPATH=$(pwd)
rm docs/_build/html/.buildinfo


%install
%py3_install


# check
# Unfortunately, the test suite relies on an incredibly old version of python-hypothesis
# (1.0.0) which is not API compatible with the version we ship in Fedora.
# nosetests-3


%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*


%files doc
%license LICENSE
%doc README.md docs/_build/html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Dan Callaghan <djc@djc.id.au> - 0.13.0-1
- New upstream release 0.13.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-7
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-6
- Subpackage python2-pymacaroons-pynacl has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Jeremy Cline <jeremy@jcline.org> - 0.9.3-1
- Initial package
