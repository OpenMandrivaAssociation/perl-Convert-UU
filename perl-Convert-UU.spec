%define upstream_name    Convert-UU
%define upstream_version 0.5201

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    UUencode and UUdecode
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
* * uuencode

  uuencode() takes as the first argument a string that is to be uuencoded.
  Note, that it is the string that is encoded, not a filename.
  Alternatively a filehandle may be passed that must be opened for reading.
  It returns the uuencoded string including 'begin' and 'end'. Second and
  third argument are optional and specify filename and mode. If unspecified
  these default to "uuencode.uu" and 644.

* * uudecode

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/puudecode
/usr/bin/puuencode
/usr/share/man/man1/puudecode.1*
/usr/share/man/man1/puuencode.1*

