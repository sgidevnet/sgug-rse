Name:		pari-galdata
Version:	20080411
Release:	16%{?dist}
Summary:	PARI/GP Computer Algebra System Galois resolvents
License:	GPLv2+
URL:		http://pari.math.u-bordeaux.fr/packages.html
Source0:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galdata.tgz
Source1:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galdata.tgz.asc
# Public key 0xb5444815, owned by Bill Allombert <allomber@math.u-bordeaux.fr>
Source2:	gpgkey-4940AE28C5F8E8A35E4D8D287833ECF1B5444815.gpg
BuildArch:	noarch

BuildRequires:	gnupg2

%description
This package contains the optional PARI package galdata, which provides
the Galois resolvents for the polgalois function, for degrees 8 through 11.

%prep
%setup -cq

# Verify the source file
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir}/pari/
cp -a data/galdata %{buildroot}%{_datadir}/pari/
%{_fixperms} %{buildroot}%{_datadir}/pari/

%files
%{_datadir}/pari/

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080411-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Jerry James <loganjerry@gmail.com> - 20080411-15
- Verify PGP signature on the source file

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080411-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080411-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080411-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080411-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080411-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20080411-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080411-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080411-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080411-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080411-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080411-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  1 2012 Paul Howarth <paul@city-fan.org> - 20080411-3
- Drop conflict with old versions of pari, which cannot use this package but
  aren't broken by it either

* Wed May 23 2012 Paul Howarth <paul@city-fan.org> - 20080411-2
- Add dist tag
- Use %%{_fixperms} to ensure packaged files have sane permissions
- At least version 2.2.7 of pari is required to use this data, so conflict
  with older versions; can't use a versioned require here as it would lead to
  circular build dependencies with pari itself

* Fri May 18 2012 Paul Howarth <paul@city-fan.org> - 20080411-1
- Initial RPM package
