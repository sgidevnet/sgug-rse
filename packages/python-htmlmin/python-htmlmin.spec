%global pypi_name htmlmin
%global desc A configurable HTML Minifier with safety features.
%global github_owner mankyd
%global github_name %{pypi_name}
%global commit 220b1d16442eb4b6fafed338ee3b61f698a01e63
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        0.1.12
Release:        8.git%{shortcommit}%{?dist}
Summary:        HTML Minifier

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{commit}/%{github_name}-%{commit}.tar.gz

BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%package       doc
Summary:       %{summary}
BuildRequires: python3-sphinx

%description  doc
%{desc}

Documentation package.


%prep
%setup -q -n %{github_name}-%{commit}
rm -rf *.egg-info


%build
%py3_build

# Build doc
cd docs
make html
make man
# Remove hidden dir in doc not to install it
rm -rf _build/html/.buildinfo


%install
%py3_install

# Install man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m0644 docs/_build/man/htmlmin.1 %{buildroot}%{_mandir}/man1


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{pypi_name}/
%{_bindir}/htmlmin
%{_mandir}/man1/*

%files doc
%license LICENSE
%doc docs/_build/html

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-8.git220b1d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-7.git220b1d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Julien Enselme <jujens@jujens.eu> - 0.1.12-6.git220b1d1
- Remove Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-5.git220b1d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.12-4.git220b1d1
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3.git220b1d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.12-2.git220b1d1
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jan 03 2018 Julien Enselme <jujens@jujens.eu> - 0.1.12-1.git220b1d1
- Update to 0.1.12

* Thu Oct 05 2017 Julien Enselme <jujens@jujens.eu> - 0.1.11-1.gitab91ff0
- Update to 0.1.11

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-6.gitcc611c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-5.gitcc611c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-4.gitcc611c3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-3.gitcc611c3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Mar 12 2016 Julien Enselme <jujens@jujens.eu> 0.1.10-2.gitcc611c3
- Remove hidden dir in doc package

* Wed Mar 09 2016 Julien Enselme <jujens@jujens.eu> - 0.1.10-1.gitcc611c3
- Initial packaging

