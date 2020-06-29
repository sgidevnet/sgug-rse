%global srcname cma
Name:           python-cma
Version:        3.0.3
Release:        2%{?dist}
Summary:        Covariance Matrix Adaptation Evolution Strategy numerical optimizer

License:        BSD
URL:            http://cma.gforge.inria.fr/cmaes_sourcecode_page.html
Source0:         %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy

%global _description \
A stochastic numerical optimization algorithm for difficult \
(non-convex, ill-conditioned, multi-modal, rugged, noisy) optimization \
problems in continuous search spaces, implemented in Python.

%description %_description

%package -n     python3-cma
Summary:        %{summary}

%description -n python3-cma %_description

%prep
%autosetup -n cma-%{version}
#Fix line-endings
sed -i 's/\r//' README.txt
#Remove unneeded shebang
sed -i '1d' cma/{bbobbenchmarks.py,purecma.py,test.py}

%build
%py3_build

%install
%py3_install

%files -n python3-cma
%doc README.md README.txt
%{python3_sitelib}/cma/
%{python3_sitelib}/cma-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.3-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Christoph Junghans <junghans@votca.org> - 3.0.3-1
- Version bump to v3.0.3 (bug #1827440)

* Tue Apr 21 2020 Christoph Junghans <junghans@votca.org> - 3.0.2-1
- Version bump to v3.0.2 (bug #1825645)

* Sun Apr 19 2020 Christoph Junghans <junghans@votca.org> - 3.0.1-1
- Version bump to v3.0.1 (bug #1825645)

* Fri Apr 17 2020 Christoph Junghans <junghans@votca.org> - 3.0.0-1
- Update to 3.0.0 (#1825359)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Christoph Junghans <junghans@votca.org> - 2.7.0-1
- Version bump to 2.7.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.7-8
- Subpackage python2-cma has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.7-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.7-1
- Update to latest version (only license file added)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.06-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.06-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 31 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.06-1
- Initial package using pyp2rpm-2.0.0
