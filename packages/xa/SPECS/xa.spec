Name:           xa
Version:        2.3.9
Release:        2%{?dist}
Summary:        6502/65816 cross-assembler

License:        GPLv2+
URL:            http://www.floodgap.com/retrotech/xa/
Source0:        http://www.floodgap.com/retrotech/%{name}/dists/%{name}-%{version}.tar.gz
# update the build system, reported in private email
Patch0:         %{name}-2.3.7-make.patch
BuildRequires:  gcc
# Perl needed for test-suite
BuildRequires:  perl-generators


%description
xa is a high-speed, two-pass portable cross-assembler. It understands
mnemonics and generates code for NMOS 6502s (such as 6502A, 6504, 6507,
6510, 7501, 8500, 8501, 8502 ...), CMOS 6502s (65C02 and Rockwell R65C02)
and the 65816.

Key amongst its features:

    * C-like preprocessor (and understands cpp for additional feature support)
    * rich expression syntax and pseudo-op vocabulary
    * multiple character sets
    * binary linking
    * supports o65 relocatable objects with a full linker and relocation suite, 
      as well as "bare" plain binary object files
    * block structure for label scoping 


%prep
%setup -q
%patch0 -p1 -b .make

# fix encoding
for f in ChangeLog doc/fileformat.txt
do
    iconv -f ISO-8859-1 -t UTF-8 < $f > $f.new
    touch -r $f $f.new
    mv $f.new $f
done


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%check
make test


%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} INSTALL="install -p"


%files
%doc COPYING ChangeLog README.1st doc/fileformat.txt
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Dan Horák <dan[at]danny.cz> - 2.3.9-1
- updated to version 2.3.9

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Dan Horák <dan[at]danny.cz> - 2.3.8-1
- updated to version 2.3.8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 03 2015 Dan Horák <dan[at]danny.cz> - 2.3.7-1
- updated to version 2.3.7
- enable test-suite

* Mon Nov 17 2014 Dan Horák <dan[at]danny.cz> - 2.3.6-1
- updated to version 2.3.6

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Dan Horák <dan[at]danny.cz> - 2.3.5-10
- spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Dan Horák <dan[at]danny.cz> - 2.3.5-3
- move the INSTALL override to "make install"
- comment the patches

* Tue Mar 31 2009 Dan Horák <dan[at]danny.cz> - 2.3.5-2
- don't use hardcoded /usr
- preserve timestamps when using "install"

* Sat Feb 21 2009 Dan Horák <dan[at]danny.cz> - 2.3.5-1
- initial Fedora version
